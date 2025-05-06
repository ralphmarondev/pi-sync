namespace PiSync.Tenant
{
    partial class TenantManageForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            panel1 = new Panel();
            btnClose = new Button();
            btnDelete = new Button();
            btnUpdate = new Button();
            btnDetails = new Button();
            panel2 = new Panel();
            label9 = new Label();
            tbImage = new TextBox();
            label7 = new Label();
            tbFingerprint = new TextBox();
            label8 = new Label();
            tbRegisteredDoors = new TextBox();
            label5 = new Label();
            tbPasswordHint = new TextBox();
            label6 = new Label();
            tbPassword = new TextBox();
            label3 = new Label();
            tbGender = new TextBox();
            label4 = new Label();
            tbUsername = new TextBox();
            label2 = new Label();
            tbLastName = new TextBox();
            label1 = new Label();
            tbFirstName = new TextBox();
            panel1.SuspendLayout();
            panel2.SuspendLayout();
            SuspendLayout();
            // 
            // panel1
            // 
            panel1.BackColor = Color.GhostWhite;
            panel1.Controls.Add(btnClose);
            panel1.Controls.Add(btnDelete);
            panel1.Controls.Add(btnUpdate);
            panel1.Controls.Add(btnDetails);
            panel1.Dock = DockStyle.Left;
            panel1.Location = new Point(0, 0);
            panel1.Name = "panel1";
            panel1.Size = new Size(241, 593);
            panel1.TabIndex = 3;
            // 
            // btnClose
            // 
            btnClose.BackColor = Color.Lavender;
            btnClose.Cursor = Cursors.Hand;
            btnClose.FlatAppearance.BorderSize = 0;
            btnClose.FlatStyle = FlatStyle.Flat;
            btnClose.Font = new Font("Courier New", 14F);
            btnClose.Location = new Point(12, 511);
            btnClose.Margin = new Padding(0);
            btnClose.Name = "btnClose";
            btnClose.Size = new Size(212, 61);
            btnClose.TabIndex = 7;
            btnClose.Text = "CLOSE";
            btnClose.UseVisualStyleBackColor = true;
            // 
            // btnDelete
            // 
            btnDelete.BackColor = Color.Lavender;
            btnDelete.Cursor = Cursors.Hand;
            btnDelete.FlatAppearance.BorderSize = 0;
            btnDelete.FlatStyle = FlatStyle.Flat;
            btnDelete.Font = new Font("Courier New", 14F);
            btnDelete.Location = new Point(12, 152);
            btnDelete.Margin = new Padding(0);
            btnDelete.Name = "btnDelete";
            btnDelete.Size = new Size(212, 61);
            btnDelete.TabIndex = 6;
            btnDelete.Text = "DELETE";
            btnDelete.UseVisualStyleBackColor = true;
            // 
            // btnUpdate
            // 
            btnUpdate.BackColor = Color.Lavender;
            btnUpdate.Cursor = Cursors.Hand;
            btnUpdate.FlatAppearance.BorderSize = 0;
            btnUpdate.FlatStyle = FlatStyle.Flat;
            btnUpdate.Font = new Font("Courier New", 14F);
            btnUpdate.Location = new Point(12, 80);
            btnUpdate.Margin = new Padding(0);
            btnUpdate.Name = "btnUpdate";
            btnUpdate.Size = new Size(212, 61);
            btnUpdate.TabIndex = 5;
            btnUpdate.Text = "UPDATE";
            btnUpdate.UseVisualStyleBackColor = true;
            // 
            // btnDetails
            // 
            btnDetails.BackColor = Color.Lavender;
            btnDetails.Cursor = Cursors.Hand;
            btnDetails.FlatAppearance.BorderSize = 0;
            btnDetails.FlatStyle = FlatStyle.Flat;
            btnDetails.Font = new Font("Courier New", 14F);
            btnDetails.Location = new Point(12, 9);
            btnDetails.Margin = new Padding(0);
            btnDetails.Name = "btnDetails";
            btnDetails.Size = new Size(212, 61);
            btnDetails.TabIndex = 4;
            btnDetails.Text = "DETAILS";
            btnDetails.UseVisualStyleBackColor = true;
            // 
            // panel2
            // 
            panel2.BackColor = SystemColors.Control;
            panel2.Controls.Add(label9);
            panel2.Controls.Add(tbImage);
            panel2.Controls.Add(label7);
            panel2.Controls.Add(tbFingerprint);
            panel2.Controls.Add(label8);
            panel2.Controls.Add(tbRegisteredDoors);
            panel2.Controls.Add(label5);
            panel2.Controls.Add(tbPasswordHint);
            panel2.Controls.Add(label6);
            panel2.Controls.Add(tbPassword);
            panel2.Controls.Add(label3);
            panel2.Controls.Add(tbGender);
            panel2.Controls.Add(label4);
            panel2.Controls.Add(tbUsername);
            panel2.Controls.Add(label2);
            panel2.Controls.Add(tbLastName);
            panel2.Controls.Add(label1);
            panel2.Controls.Add(tbFirstName);
            panel2.Location = new Point(268, 23);
            panel2.Name = "panel2";
            panel2.Size = new Size(694, 495);
            panel2.TabIndex = 4;
            // 
            // label9
            // 
            label9.AutoSize = true;
            label9.Font = new Font("Courier New", 11F);
            label9.Location = new Point(41, 399);
            label9.Name = "label9";
            label9.Size = new Size(76, 21);
            label9.TabIndex = 21;
            label9.Text = "Image:";
            // 
            // tbImage
            // 
            tbImage.BackColor = SystemColors.Window;
            tbImage.Location = new Point(41, 426);
            tbImage.Name = "tbImage";
            tbImage.PlaceholderText = "Not implement yet. Can leave as null";
            tbImage.ReadOnly = true;
            tbImage.Size = new Size(606, 30);
            tbImage.TabIndex = 20;
            // 
            // label7
            // 
            label7.AutoSize = true;
            label7.Font = new Font("Courier New", 11F);
            label7.Location = new Point(41, 326);
            label7.Name = "label7";
            label7.Size = new Size(142, 21);
            label7.TabIndex = 19;
            label7.Text = "Fingerprint:";
            // 
            // tbFingerprint
            // 
            tbFingerprint.BackColor = SystemColors.Window;
            tbFingerprint.Location = new Point(41, 353);
            tbFingerprint.Name = "tbFingerprint";
            tbFingerprint.PlaceholderText = "Not implement yet. Can leave as null";
            tbFingerprint.ReadOnly = true;
            tbFingerprint.Size = new Size(606, 30);
            tbFingerprint.TabIndex = 18;
            // 
            // label8
            // 
            label8.AutoSize = true;
            label8.Font = new Font("Courier New", 11F);
            label8.Location = new Point(41, 247);
            label8.Name = "label8";
            label8.Size = new Size(197, 21);
            label8.TabIndex = 17;
            label8.Text = "Registered Doors:";
            // 
            // tbRegisteredDoors
            // 
            tbRegisteredDoors.BackColor = SystemColors.Window;
            tbRegisteredDoors.Location = new Point(41, 274);
            tbRegisteredDoors.Name = "tbRegisteredDoors";
            tbRegisteredDoors.PlaceholderText = "If more than 1, separate by comma. Ex. A14, A15";
            tbRegisteredDoors.ReadOnly = true;
            tbRegisteredDoors.Size = new Size(606, 30);
            tbRegisteredDoors.TabIndex = 16;
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Font = new Font("Courier New", 11F);
            label5.Location = new Point(358, 165);
            label5.Name = "label5";
            label5.Size = new Size(164, 21);
            label5.TabIndex = 15;
            label5.Text = "Password Hint:";
            // 
            // tbPasswordHint
            // 
            tbPasswordHint.BackColor = SystemColors.Window;
            tbPasswordHint.Location = new Point(358, 192);
            tbPasswordHint.Name = "tbPasswordHint";
            tbPasswordHint.PlaceholderText = "Optional";
            tbPasswordHint.ReadOnly = true;
            tbPasswordHint.Size = new Size(289, 30);
            tbPasswordHint.TabIndex = 14;
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.Font = new Font("Courier New", 11F);
            label6.Location = new Point(41, 165);
            label6.Name = "label6";
            label6.Size = new Size(109, 21);
            label6.TabIndex = 13;
            label6.Text = "Password:";
            // 
            // tbPassword
            // 
            tbPassword.BackColor = SystemColors.Window;
            tbPassword.Location = new Point(41, 192);
            tbPassword.Name = "tbPassword";
            tbPassword.ReadOnly = true;
            tbPassword.Size = new Size(289, 30);
            tbPassword.TabIndex = 12;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Font = new Font("Courier New", 11F);
            label3.Location = new Point(358, 89);
            label3.Name = "label3";
            label3.Size = new Size(87, 21);
            label3.TabIndex = 11;
            label3.Text = "Gender:";
            // 
            // tbGender
            // 
            tbGender.BackColor = SystemColors.Window;
            tbGender.Location = new Point(358, 116);
            tbGender.Name = "tbGender";
            tbGender.ReadOnly = true;
            tbGender.Size = new Size(289, 30);
            tbGender.TabIndex = 10;
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Font = new Font("Courier New", 11F);
            label4.Location = new Point(41, 89);
            label4.Name = "label4";
            label4.Size = new Size(109, 21);
            label4.TabIndex = 9;
            label4.Text = "Username:";
            // 
            // tbUsername
            // 
            tbUsername.BackColor = SystemColors.Window;
            tbUsername.Location = new Point(41, 116);
            tbUsername.Name = "tbUsername";
            tbUsername.ReadOnly = true;
            tbUsername.Size = new Size(289, 30);
            tbUsername.TabIndex = 8;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Font = new Font("Courier New", 11F);
            label2.Location = new Point(358, 15);
            label2.Name = "label2";
            label2.Size = new Size(120, 21);
            label2.TabIndex = 7;
            label2.Text = "Last Name:";
            // 
            // tbLastName
            // 
            tbLastName.BackColor = SystemColors.Window;
            tbLastName.Location = new Point(358, 42);
            tbLastName.Name = "tbLastName";
            tbLastName.ReadOnly = true;
            tbLastName.Size = new Size(289, 30);
            tbLastName.TabIndex = 6;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("Courier New", 11F);
            label1.Location = new Point(41, 15);
            label1.Name = "label1";
            label1.Size = new Size(131, 21);
            label1.TabIndex = 5;
            label1.Text = "First Name:";
            // 
            // tbFirstName
            // 
            tbFirstName.BackColor = SystemColors.Window;
            tbFirstName.Location = new Point(41, 42);
            tbFirstName.Name = "tbFirstName";
            tbFirstName.ReadOnly = true;
            tbFirstName.Size = new Size(289, 30);
            tbFirstName.TabIndex = 4;
            // 
            // TenantManageForm
            // 
            AutoScaleDimensions = new SizeF(12F, 22F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(988, 593);
            Controls.Add(panel2);
            Controls.Add(panel1);
            Font = new Font("Courier New", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            FormBorderStyle = FormBorderStyle.FixedToolWindow;
            Margin = new Padding(4, 4, 4, 4);
            Name = "TenantManageForm";
            StartPosition = FormStartPosition.CenterParent;
            Text = "MANAGE TENANT";
            panel1.ResumeLayout(false);
            panel2.ResumeLayout(false);
            panel2.PerformLayout();
            ResumeLayout(false);
        }

        #endregion

        private Panel panel1;
        private Button btnClose;
        private Button btnDelete;
        private Button btnUpdate;
        private Button btnDetails;
        private Panel panel2;
        private Label label9;
        private TextBox tbImage;
        private Label label7;
        private TextBox tbFingerprint;
        private Label label8;
        private TextBox tbRegisteredDoors;
        private Label label5;
        private TextBox tbPasswordHint;
        private Label label6;
        private TextBox tbPassword;
        private Label label3;
        private TextBox tbGender;
        private Label label4;
        private TextBox tbUsername;
        private Label label2;
        private TextBox tbLastName;
        private Label label1;
        private TextBox tbFirstName;
    }
}